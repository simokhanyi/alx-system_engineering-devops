#!/usr/bin/env ruby
#The regular expression must be only matching: capital letters

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <string>"
  exit 1
end

# Get the argument passed to the script
input_string = ARGV[0]

# Define the regular expression pattern to match capital letters
pattern = /[A-Z]/

# Extract all matched capital letters from the input string
matched_letters = input_string.scan(pattern).join('')

# Output the matched capital letters or an empty string if not found
puts matched_letters.empty? ? '' : matched_letters
