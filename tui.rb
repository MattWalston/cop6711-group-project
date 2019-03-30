#!/usr/bin/env ruby

require 'pry' if ENV['RUBY_ENV'] == 'development'

require_relative 'subject'
require_relative 'terms'

puts "Supply message to parse (LF submits):" if STDIN.tty?
body = gets

subject = Subject.new body
terms = subject.related_to_features Terms.instance.terms
puts terms.count > 1 ? terms : 'No features identified.'

