#!/usr/bin/env ruby

require 'pry' if ENV['RUBY_ENV'] == 'development'

require 'sinatra'
require_relative 'terms'
require_relative 'subject'

get '/' do
  body = params['body']&.strip
  terms = []

  if body
    subject = Subject.new body
    terms = subject.related_to_features Terms.instance.terms
  end

  erb :index, locals: { body: body, terms: terms}
end
