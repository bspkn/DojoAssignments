function finalCountdown(param1, param2, param3, param 4) {
  var mult = param1;
  var start = param2;
  var end = param3;
  var skip = param4;
}


var mult = param1;\
var start = param2;\
var end = param3;\
var skip = param4;\
\
var direction = start > end ? 'down' : 'up';\
function comparer(start, end)\
if (direction == 'down') \{\
return start <= end;\
\} else \{\
  return start >= end;\
\}\
\}\
\
//start at start, end at end\
for (start; comparer(start, end); start++) \{\
  if (start%mult === 0)\{\
    if (start !== skip)\{\
      console.log(start);\
    \}\
  \}\
\}\
\
\}\
finalCountdown(3,5,17,9)}
