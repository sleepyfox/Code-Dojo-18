if (typeof module) is 'undefined' # means running in the browser
  console.log 'running in the browser'
  chai.should()
  f = this.fibonacci 
else
  console.log 'running in node'
  should = require('chai').should()
  f = require './fibonacci.js'

someFunc = f.someFunc


describe 'A test suite', ->
  it 'someFunc should be true', ->
    someFunc().should.equal true

  describe 'A string of fifteen letters', ->
    myString = "Now is the time"

    it 'should be of type string', ->
      myString.should.be.a 'string'

    it 'should have a length of 15', ->
      myString.should.have.length 15
      
  describe 'An array of three items', ->
    array = [1, 2, 3]

    it 'should be of type array', ->
      array.should.be.a 'array'

    it 'should have a length of 3', ->
      array.should.have.length 3

    it 'should return -1 when a searched for item is not present', ->
      array.indexOf(4).should.equal -1

describe 'Graph tests', ->
  describe 'A graph with a single node', ->
    it 'should starting at A and finishing at A have a length of zero', ->
      route = { 
        length: -> 0
      }
      route.length().should.equal 0

  describe 'A graph with two nodes', ->
    it 'should have a length of one', ->
      route = { 
        itinerary: ['A', 'F'],
        length: -> @itinerary.length - 1
      }
      route.length().should.equal 1


