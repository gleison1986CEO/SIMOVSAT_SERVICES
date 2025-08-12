const fs     = require('node:fs');


module.exports.LOGS = function (logs){
    
  if(logs != null || logs != ''){
      const content = logs.toString();
      var datetime = new Date();
      var rand = Math.floor(Math.random() * 10000000000);

      try {
        fs.writeFileSync('./datalog/'+ datetime.toString() + '_' + rand.toString() + '.txt', content);
      } catch (err) {
        console.error(err);
      }
      return content;
  }
}
