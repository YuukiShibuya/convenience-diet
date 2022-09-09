// document.currentScript.insertAdjacentHTML('beforebegin', '<p>Hello</p>');

// document.currentScript.insertAdjacentHTML('beforebegin', '<p>Bye</p>');

/* id = targetの属性に対して、コンテンツを指定する */
/* id属性よりも下に記載する必要あり */
//let element = document.getElementById('target');
//element.innerHTML = 'Good bye bye';

function getElement(){
  let shop = document.getElementById('shop');
  //console.log('shop: ' + shop.textContent);

  let cal = document.getElementById('cal');
  //console.log('cal: ' + cal.textContent);

  let price = document.getElementById('price');
  //console.log('price: ' + price.textContent);

  let item = document.getElementById('item');
  //console.log('item: ' + item.textContent);

  let req = [shop.textContent,cal.textContent,price.textContent,item.textContent];
  console.log(req);
}
