#!/usr/bin/env ruby

require 'pry' if ENV['RUBY_ENV'] == 'development'

require 'sinatra'
require_relative 'terms'
require_relative 'subject'

class String
  def titlecase
    split(/([[:alpha:]]+)/).map(&:capitalize).join
  end
end

get '/' do
  body = params['body']&.strip
  terms = []

  if body
    subject = Subject.new body
    terms = subject.related_to_features Terms.instance.terms
    if terms.count > 0
      term = "Smart #{terms&.first.titlecase}"
    else
      term = ''
    end
  end

  erb :index, locals: { body: body, term: term}
end
