#!/usr/bin/env ruby
#Sript that run some statistics on the TextMe app text messages transactions.

# Check if the argument is provided
if ARGV.empty?
  puts "Usage: #{$PROGRAM_NAME} <log_file>"
  exit 1
end

# Get the log file path from the command line argument
log_file = ARGV[0]

# Read the log file line by line
File.foreach(log_file) do |line|
  # Extracting relevant information using regular expressions
  sender = line.match(/\[from:([^ \]]+)\]/)&.captures&.first || ""
  receiver = line.match(/\[to:([^ \]]+)\]/)&.captures&.first || ""
  flags = line.match(/\[flags:([^ \]]+)\]/)&.captures&.first || ""

  # Output the extracted information
  next if [sender, receiver, flags].any?(&:empty?)
  puts "#{sender},#{receiver},#{flags}"
end
