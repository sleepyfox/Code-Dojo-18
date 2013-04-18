someFunc = ->
  true

if (typeof module) is 'undefined'
  f = {}
  f.someFunc = someFunc
  @fibonacci = f 
else
  # CommonsJS module definitions
  exports.someFunc = someFunc
  