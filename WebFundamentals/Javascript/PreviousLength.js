var prev = arr[length - 1].length
var cur; // current index length
  function prevLength(arr) {
    for (var i = 0; i < arr.length; i++) {
      cur = arr[i].length;
      arr[i] = prev;
      prev = cur;
  }
  return arr;
}
var test =['a', 'aa' , 'aaa' , 'aaaa' ]
console.log(test);
