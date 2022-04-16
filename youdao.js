var CryptoJS = require('./crypto-js'); // 使用node.js导入crypto-js包？

//通过对页面进行debugger，data为翻译的内容

function getEncryptedParams(data,ua){
    var bv = CryptoJS.MD5(ua).toString()
      , lts = "" + (new Date).getTime()
      , salt = lts + parseInt(10 * Math.random(), 10);
    var sign = CryptoJS.MD5("fanyideskweb" + data + salt + "Ygy_4c=r#e#4EX^NUGUc5").toString() //toString函数把装换成字符串
    return {
        bv: bv,
        lts: lts,
        salt: salt,
        sign: sign
    }
};

// var data = "测试";
// var ua = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36";
// console.log(getEncryptedParams(data,ua));