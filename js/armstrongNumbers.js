// How can you make this more scalable and reusable later?

exports.findArmstrongNumbers = function(numbers) {
    let armstrongNumbers = [];

    for(let i=0; i<numbers.length; i++) {
        let digits = String(i).split('');
        let sum = 0;
        for(let i=0; i<digits.length; i++) {
            sum += Math.pow(digits[i], digits.length)
        }

        if(sum == numbers[i]) {
            armstrongNumbers.push(numbers[i]);
        }
    }

    return armstrongNumbers;
};