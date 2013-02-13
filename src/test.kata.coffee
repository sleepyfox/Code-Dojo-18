chai.should()

describe 'A test suite', ->
  describe 'A string of fifteen letters', ->
    it 'should have a length of 15', ->
      "Now is the time".should.have.length 15
      
  describe 'An array of three items', ->
    array = [1, 2, 3]

    it 'should have a length of 3', ->
      array.should.have.length 3

    it 'should return -1 when a searched for item is not present', ->
      array.indexOf(4).should.equal -1

