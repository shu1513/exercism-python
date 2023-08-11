// @ts-check

/**
 * Calculates the sum of the two input arrays.
 *
 * @param {number[]} array1
 * @param {number[]} array2
 * @returns {number} sum of the two arrays
 */
export function twoSum(array1, array2) {
  return Number(array1.join('')) + Number(array2.join(''));
}

/**
 * Checks whether a number is a palindrome.
 *
 * @param {number} value
 * @returns {boolean} whether the number is a palindrome or not
 */
export function luckyNumber(value) {
  let strvalue = String(value);
  for (let i = 0; i < (strvalue.length / 2); i++) {
    if (strvalue[i] != strvalue[strvalue.length - i - 1]) {
      return false;
    }
  }
  return true;

}

/**
 * Determines the error message that should be shown to the user
 * for the given input value.
 *
 * @param {string|null|undefined} input
 * @returns {string} error message
 */
export function errorMessage(input) {
  if (input == '' || input == undefined || input == null) {
    return 'Required field';
  }
  else if (Number(input) == 0 || isNaN(Number(input))) {
    return 'Must be a number besides 0';
  }
  else {
    return '';
  }

}

