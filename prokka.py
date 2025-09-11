import os
import subprocess

input_dir = 'input'
output_dir = 'output'

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

for filename in os.listdir(input_dir):
    basename, extension = os.path.splitext(filename)
    if extension:
        prokka_cmd = ['prokka',
                      '--kingdom', 'Bacteria',
                      '--strain', basename,
                      '--gcode', '11',
                      '--compliant',
                      '--addgenes',
                      '--mincontiglen', '200',
                      '--rfam',
                      '--centre', 'CLIENT',
                      '--cpus', '5',
	              '--prefix', basename,
                      '--outdir', os.path.join(output_dir, basename),
                      os.path.join(input_dir, filename)]
        subprocess.run(prokka_cmd)
