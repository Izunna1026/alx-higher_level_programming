#!/usr/bin/node
const dict = require('./101-data').dict;

const totalist = Object.entries(dict);
const vals = Object.values(dict);
const valsUniq = [...new set(vals)];
const newDict = {};
for (const d in valsUniq) {
  const list = [];
  for (const y in totalist) {
    if (totalist[y][1] === valsUniq[d]) {
      list.unshift(totalist[y][0]);
    }
  }
  newDict[valsUniq[d]] = list;
}
console.log(newDict);

