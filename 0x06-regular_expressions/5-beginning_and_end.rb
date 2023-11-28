#!/usr/bin/env ruby
#script that accepts one args and pass it to regular expression matching method

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the argument passed to the script
input_string = ARGV[0]

# Define the regular expression pattern
pattern = /^h.n$/

# Match the pattern in the input string
match_result = input_string.match(pattern)

# Output the matched result or an empty string if not found
puts match_result ? match_result[0] : ''
