#!/usr/bin/env ruby
#Regular expression must match a 10 digit phone number

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the argument passed to the script
input_string = ARGV[0]

# Define the regular expression pattern to match a 10-digit phone number
pattern = /^\d{10}$/

# Match the pattern in the input string
match_result = input_string.match(pattern)

# Output the matched result or an empty string if not found
puts match_result ? match_result[0] : ''
