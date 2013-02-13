chai.should()

describe 'A test suite', ->
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

