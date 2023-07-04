#!/usr/bin/env ruby
# A regular expression that extracts sender, receiver & flags and outputs the info
puts ARGV[0].scan(/\[from:(.*?)\]\s\[to:(.*?)\]\s\[flags:(.*?)\]/).flatten.join(",")
