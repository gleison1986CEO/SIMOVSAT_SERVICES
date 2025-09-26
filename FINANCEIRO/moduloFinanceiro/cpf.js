// REGEX CPF

module.exports.CPF = function (cpf){

    String.prototype.isNumber = function(){
                return /^\d+$/.test(this);
    } 
    return cpf.isNumber();
}

// REGEX CPF
