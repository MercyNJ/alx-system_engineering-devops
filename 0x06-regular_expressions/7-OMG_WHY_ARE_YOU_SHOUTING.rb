#!/usr/bin/env ruby
# A regular expression that matches ONLY capital letters
puts ARGV[0].scan(/[A-Z]/).join
