#!/usr/bin/env ruby
# A regular expression that matches given cases utilizing repetition token
puts ARGV[0].scan(/hbt{1,4}n/).join
