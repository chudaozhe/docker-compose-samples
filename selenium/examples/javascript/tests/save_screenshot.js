const { Builder, By, Capabilities } = require("selenium-webdriver");

let fs = require('fs');

(async function example() {
    let driver = new Builder()
        .usingServer("http://localhost:4444/wd/hub")
        .withCapabilities(Capabilities.chrome())
        .build();

    await driver.get('https://www.baidu.com');
    await driver.findElement(By.id('kw')).sendKeys('自动化测试haha1');
    // Returns base64 encoded string
    let encodedString = await driver.takeScreenshot();
    await fs.writeFileSync('./baidu.png', encodedString, 'base64');
    await driver.quit();
}())
