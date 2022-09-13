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
