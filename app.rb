require 'sinatra'
require 'google/cloud/language'

require 'logger'

module MyLogger
  LOGGER = Logger.new $stderr, level: Logger::WARN
  def logger
    LOGGER
  end
end

module GRPC
  extend MyLogger
end

get '/' do
  tweet_body = params['tweet-body'].strip
  response = ''
  unless tweet_body == nil  || tweet_body == ''
    language_services_client = Google::Cloud::Language.new version: :v1
    document = { content: tweet_body, type: :PLAIN_TEXT }
    response = language_services_client.analyze_entity_sentiment(document)
  end
  erb :index, locals: { tweet_body: tweet_body, ordinances: response}
end