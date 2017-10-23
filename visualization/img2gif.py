"""
cd dir_imgs_git

# from images to an avi
ffmpeg -i git_tool%d.png out.avi

# from avi to a slow down, if there are only a few images
# increase 4.0, 16.0, 64, 128 to slow down
ffmpeg -i out.avi -filter:v setpts=128.0*PTS out_dn.avi

# from avi to a speed_up avi, if there are a lot of images
# decrease from 1.0 to 0.5, 0.25, 0.1, 0.05 to speed up
ffmpeg -i out.avi -filter:v setpts=0.25*PTS out_up.avi

# from avi to gif
ffmpeg -i out_up.avi out_up.gif
"""

import argparse
import sys
import os
import subprocess

def img2gif(args):
	os.chdir(args.plots_path)
	# epoch_%d0.png: only takes epoch_0|10|20|30...|100|110
	# epoch_%d.png: only takes epoch_0|1|2|3...
	# epoch_%d5.png: only takes epoch_5|15|25|35...|105|115
	subprocess.call(['ffmpeg', '-i', 'git_tool%d.png', 'out.avi'])
	subprocess.call(['ffmpeg', '-i', 'out.avi', '-filter:v', 'setpts=128.0*PTS', 'out_dn.avi'])
	subprocess.call(['ffmpeg', '-i', 'out_dn.avi', '-filter:v', 'setpts=0.25*PTS', 'out_up.avi'])
	subprocess.call(['ffmpeg', '-i', 'out_dn.avi', 'out_dn.gif'])
	subprocess.call(['ffmpeg', '-i', 'out_up.avi', 'out_up.gif'])
	subprocess.call(['ffmpeg', '-i', 'out.avi', 'out.gif'])

def build_parser():
	""" Constructs an argument parser and returns the parsed arguments.
	"""
	# start: description
	parser = argparse.ArgumentParser(description='my argparse tool')
	# create a command line function
	subparsers = parser.add_subparsers(dest='cmd', help='Sub-command help.')

	#########################################################
	subparser = subparsers.add_parser('img2gif', help='conver images to gif with 3 speeds')
	subparser.add_argument('-img_dir', required=True, help="Path to save plots")
	subparser.set_defaults(func=img2gif)

	return parser, subparsers


def parse_args(parser):
	""" Parses command-line arguments.
	"""
	return parser.parse_args()

def main():
	parser, _ = build_parser()
	args = parse_args(parser)

	sys.exit(args.func(args) or 0)

if __name__ == '__main__':
	main()

# run the line below in terminal
# python 101_img2gif.py -img_dir dir_images_stored
