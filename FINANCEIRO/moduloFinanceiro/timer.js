module.exports.TIMER = function (){
    const timer = ms => new Promise(res => setTimeout(res, ms))
    return timer(23000);
    
}
