#!/usr/bin/node
function factorial(n) {
  const num = parseInt(n);
  if (Number.isNaN(num) || num <= 1) return 1;
  return num * factorial(num - 1);
}
console.log(factorial(process.argv[2]));
