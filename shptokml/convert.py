"""
Converts SHP file to KML.
"""

import argparse
import subprocess

def main():
  """
  Converts the SHP file to KML
  """

  arguments = load_command_line_arguments()

  convert_shp_to_kml(arguments.input, arguments.output)


def load_command_line_arguments():
  """
  Load command-line arguments.
  """
  parser = argparse.ArgumentParser(description='Converts SHP files to KML.')
  parser.add_argument('--input', '-i', required=True,
                      help='the SHP file to convert')
  parser.add_argument('--output', '-o', default='output.kml',
                      help='the KML file to output to')
  args = parser.parse_args()
  return args


def convert_shp_to_kml(input_path, output_path):
  """
  Converts SHP to KML
  """
  convert_binary = 'ogr2ogr'

  try:
    completed_process = subprocess.run(
      [convert_binary,'-f','KML', output_path, input_path],
      stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
  except FileNotFoundError:
    print("The program '%s' is missing. You need to have that installed " +
          "in order to use this script." % convert_binary)
  else:
    print(completed_process.stdout.decode("utf-8"))
    return completed_process.returncode

if __name__ == "__main__":
  main()