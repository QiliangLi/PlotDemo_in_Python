#!/usr/bin/env python

import sys
import os
import argparse
import subprocess
import threading

TEMP_DIR = './.draw_cdf'

def parse_args():
	parser = argparse.ArgumentParser()
	parser.add_argument('src', nargs='+', help='Source file(s)')
	parser.add_argument('-t', '--title', help='Title of the CDF graph')
	parser.add_argument('-x', '--xlabel', help='Label for X axis')
	parser.add_argument('-l', '--logx', help='Set x axis to logscale', action='store_true')
	parser.add_argument('-p', '--numpat', help='Pattern to print number into gnuplot script. E.g. %%d')
	return parser.parse_args()

def show_text(text, tag='MAIN'):
	if not isinstance(text, str) or not isinstance(tag, str):	return
	lines = text.split('\n')
	for line in lines:
		print '\033[1;32m[%s]\033[0m %s' % (tag, line)

def show_prompt(prompt, tag='MAIN'):
	if not isinstance(prompt, str) or not isinstance(tag, str):	return
	print '\033[1;32m[%s]\033[1;33m %s\033[0m' % (tag, prompt)

def show_error(prompt):
	if not isinstance(prompt, str):	return
	print '\033[1;31m[ERROR]\033[1;35m %s\033[0m' % prompt

def tostring(number, args):
	return args.numpat and (args.numpat % number) or str(number)

def call_shell(cmd):
	if not cmd:	return None, None
	subp = subprocess.Popen(cmd, shell=True,\
			stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	return subp.communicate()

class HandledData(object):
	def __init__(self, name, path, sorted_path, medium_value,\
				 average, avg_ln, total_lines, p99_value):
		self.name = name
		self.path = path
		self.sorted_path = sorted_path 
		self.medium_value = medium_value 
		self.average = average 
		self.avg_ln = avg_ln 
		self.total_lines = total_lines 
		self.p99_value = p99_value 

	def gen_labels(self, args, next_label = 1):
		return """set label %d "Medium" at %s,0.5 point pointtype 7 pointsize 1.5
set label %d "Avg" at %s,%.2f point pointtype 7 pointsize 1.5
set label %d "P99" at %s,0.99 point pointtype 7 pointsize 1.5
"""\
		% ( next_label, tostring(self.medium_value, args),\
			next_label + 1, tostring(self.average, args), float(self.avg_ln) / self.total_lines,\
			next_label + 2, tostring(self.p99_value, args) ), next_label + 3

	def gen_plot(self, next_lt = 1):
		return '"%s" using (($1)):(1./%d.) with linespoints title \'%s\' lw 2 lt %d smooth cumulative'\
		% (self.sorted_path, self.total_lines, self.name.replace('_', '\\_'), next_lt), next_lt + 1

def handle_single_file(src, collector, args):
	src_dn = os.path.dirname(src)
	src_bn = os.path.basename(src)
	sorted_src = src_dn + (src_dn and '/sorted_' or 'sorted_') + src_bn

	# Get name
	dot_rindex = src_bn.rfind('.')
	src_name = dot_rindex < 0 and src_bn or src_bn[:dot_rindex]

	# Tag
	tag = src_name

	# Sort
	sorted_src = os.path.join(TEMP_DIR, 'sorted_%s' % src.replace('/', '_'))
	call_shell('sort -n %s -o %s' % (src, sorted_src))

	show_prompt('Counting lines and calculating average...', tag);
	cmd = 'awk \'{sum+=$1} END {print NR; print sum/NR}\' %s' % sorted_src
	out, err = call_shell('awk \'{sum+=$1} END {print NR; print sum/NR}\' %s' % sorted_src)
	if err:
		show_error(err)
		return 0
	filedata = out.split()
	total_lines = int(filedata[0])
	average = float(filedata[1])
	show_prompt('Searching for medium value, P99 value and line number of average', tag)
	medium_ln = total_lines / 2
	avg_ln = -1
	p99_ln = int(0.99 * float(total_lines))
	fin = open(sorted_src, 'r')
	line_count = 0
	while True:
		# Read line
		line = fin.readline()
		if not line:	break
		line_count += 1
		line = line[:-1]

		# Parse string to number
		try:
			line_dat = int(line)
		except ValueError:
			try:
				line_dat = float(line)
			except ValueError:
				show_error('Line %d: Illegal string %s' % (line_count, line))
				return

		# Check medium
		if line_count == medium_ln:
			medium_value = line_dat

		# Check average
		if avg_ln < 0 and line_dat >= average:
			avg_ln = line_count

		# Check P99
		if line_count == p99_ln:
			p99_value = line_dat
			break # We assume this is the last line we concern
	fin.close()
	show_text('Total lines: %d\nAverage: %s\nMedium: %s\nP99: %s'\
			% (total_lines, tostring(average, args),\
			tostring(medium_value, args), tostring(p99_value, args)), tag)

	collector.append(HandledData(src_name, src, sorted_src, medium_value,\
								 average, avg_ln, total_lines, p99_value))

def main():
	if os.path.isfile(TEMP_DIR):
		os.remove(TEMP_DIR)
	
	if not os.path.exists(TEMP_DIR):
		os.mkdir(TEMP_DIR)

	args = parse_args()

	show_prompt('Sorting the original file...');

	collector = []
	thread_pool = []
	for single_src in args.src:
		t = threading.Thread(target=handle_single_file, args=(single_src, collector, args))
		t.start()
		thread_pool.append(t)

	for t in thread_pool:
		t.join()

	# Generate GNUPLOT script
	show_prompt("Generating script ...")
	script_templ = """set ylabel "CDF"
set yrange [0:1]
set ytics 0.2
set key bottom right
set style rect fc lt -1 fs solid 0.15 noborder
set grid"""
	script_path = os.path.join(TEMP_DIR, 'draw-cdf.plot')
	gp_fout = open(script_path, 'w')
	if not gp_fout:
		print 'Could not write scripts to file draw-cdf.plot.'
		return -1
	if args.title:
		gp_fout.write('set title \"%s\"\n' % args.title)
	if args.logx:
		gp_fout.write('set logscale x\n')
	if args.xlabel:
		gp_fout.write('set xlabel \"%s\"\n' % args.xlabel)

	gp_fout.write('%s\n' % script_templ)
	
	assert len(collector) > 1
	next_label = 1
	for data_item in collector:
		script_cmd, next_label = data_item.gen_labels(args, next_label)
		gp_fout.write(script_cmd)

	gp_fout.write('plot %s' % collector[0].gen_plot()[0])
	collector = collector[1:]
	next_lt = 2
	for data_item in collector:
		script_cmd, next_lt = data_item.gen_plot(next_lt)
		gp_fout.write(',\\\n\t%s' % script_cmd)
	gp_fout.close()

	show_prompt('Drawing CDF graph with GNUPLOT')
	out, err = call_shell('gnuplot -p %s' % script_path)
	if err:
		show_error(err)

	return 0

if __name__ == '__main__':
	sys.exit(main())
