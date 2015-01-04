from subprocess import *
import sys, os, errno, getopt, time, datetime

DEVELOPER_MODE = True
TIMESTAMP_FORMAT = '%m-%d-%Y__%H:%M:%S-'

def setup(path):
	try:
		os.makedirs(path + 'grader')
	except OSError as exception:
		if exception.errno != errno.EEXIST:
			raise
	try:
		os.chdir(path)
	except:
		print "cannot change directory"

def build():
	make_commands = ['clean', 'webserver', 'webclient']
	commands = []

	for make_command in make_commands:
		commands.append(['make', make_command])

	for idx, command in enumerate(commands):
		try:
			if DEVELOPER_MODE:
				stdout_file = open('grader/make_' + make_commands[idx] + '_stdout.txt', 'w+')
				stderr_file = open('grader/make_' + make_commands[idx] + '_stderr.txt', 'w+')
			else:
				stdout_file = open('grader/' + time.strftime(TIMESTAMP_FORMAT) + 'make_' + make_commands[idx] + '_stdout.txt', 'w+')
				stderr_file = open('grader/' + time.strftime(TIMESTAMP_FORMAT) + 'make_' + make_commands[idx] + '_stderr.txt', 'w+')	
			p = Popen(command, stdout = stdout_file, stderr = stderr_file)
			poutput = p.communicate()[0]
			if p.returncode != 0:				
				raise CalledProcessError
		except CalledProcessError, e:
			raise
		else:
			stdout_file.close()
			stderr_file.close()	

def parse_args(argv):
	try:
		opts, args = getopt.getopt(argv, "hp:", ["help", "project_path="])
	except getopt.GetoptError:
		help_menu()
		sys.exit(2)
	for opt, arg in opts:
		if opt in ("-h", "--help"):
			help_menu()
			sys.exit(2)
		elif opt == '-p':
			if os.path.exists(arg):			
				return arg
	if(len(opts) == 0):
		help_menu()
		sys.exit(2)

def help_menu():
	print 'usage: pr1-grader.py -p <project_dir>'

def main(argv):	
	project_path = parse_args(argv)
	setup(project_path)
	build()	

if __name__ == "__main__":
   main(sys.argv[1:])