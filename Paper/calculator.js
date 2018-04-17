function addition(addend1, addend2){
  return Number(addend1) + Number(addend2);
}

function subtraction(minuend, subtrahend){
  return Number(minuend) - Number(subtrahend);
}

function multiplication(factor1, factor2){
  return Number(factor1) * Number(factor2);
}

function division(dividend, divisor){
  if(divisor === 0){
    console.log("Can't divide by zero!");
    return dividend;
  }
  else{
    return Number(dividend) / Number(divisor);
  }
}

function power(base, exponent){
  let product = 1;
  for(let i = 1; i <= exponent; i++){
    product *= Number(base);
  }
  return product
}

function getNumber(useTotal, total){
  let result = readline().trim();
  if(result === "exit"){
    return result;
  }
  if(result === useTotal){
    result = total;
  }
  while(isNaN(Number(result))){
    console.log(result + " is not a number, please insert a number.");
    result = readline();
  }
  return result;
}

function helper(){
  console.log(`Valid operations are '${sum}' to do the addition, ${diff} to subtract, ${mult} to multiply,\n${div} to divide, ${pow} to do the power.\n${useTotal} if you want to use the total as the value: Note that you have to use this command when inserting a numeric value, and not an operation.`);
}

function calculator(){
  let sum = "+", diff = "-", mult = "*", div = "/", pow = "^", useTotal = "ans", closeOperation = "exit", help = "help";
  let total = 0;
  let firstValue = 0;
  let secondValue = 0;
  let operation = "";
  let exit = false;
  while (!exit){
    operation = "";
    console.log("Insert the first number: ");
    firstValue = getNumber(useTotal, total);
    exit = (firstValue === closeOperation);
    if(exit){
      break;
    }
    while(operation !== sum && operation !== diff && operation !== mult && operation !== div && operation !== pow && operation !== help){
      console.log("Insert the operator:");
      operation = readline().trim();
      exit = (operation === closeOperation);
      if(exit){
        break;
      }
    }
    if(exit){
      break;
    }
    if(operation === help){
      helper();
      continue;
    }
    console.log("Insert the second number: ");
    secondValue = getNumber(useTotal, total);
    exit = (secondValue === closeOperation);
    if(exit){
      break;
    }
    switch (operation) {
      case sum: total = addition(firstValue, secondValue);
                break;
      case diff: total = subtraction(firstValue, secondValue);
                 break;
      case mult: total = multiplication(firstValue, secondValue);
                 break;
      case div: total = division(firstValue, secondValue);
                break;
      case pow: total = power(firstValue, secondValue);
                break;
      default: console.log("unexpected command. If you reached this message, something went really wrong.");
    }
    console.log("The total is: " + total);
    console.log("\n")
  }
  console.log("Goodbye.");
}
