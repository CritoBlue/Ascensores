fetch('http://127.0.0.1:8000/getdata').then(function(response){
	return response.json();
}).then(function(jsondata){
	dbPromise.then(function(db){
		var tx = db.transaction('ordenes', 'readwrite');
		var ordenesStore = tx.objectStore('ordenes');
		for(var key in jsondata){
			if (jsondata.hasOwnProperty(key)) {
				ordenesStore.put(jsondata[key]); 
			}
		}
	});
});

var dbPromise = idb.open('ordenes-db', 1, function(upgradeDb) {
	upgradeDb.createObjectStore('ordenes',{keyPath:'pk'});
});

var post="";
 dbPromise.then(function(db){
  var tx = db.transaction('ordenes', 'readonly');
    var ordenesStore = tx.objectStore('ordenes');
    return ordenesStore.openCursor();
 }).then(function logItems(cursor) {
    if (!cursor) {
     document.getElementById('offlinedata').innerHTML=post;
      return;
    }
    for (var field in cursor.value) {
       if(field=='fields'){
        ordenesData=cursor.value[field];
        for(var key in ordenesData){
         if(key =='idOT'){
          var idOT = '<h3>'+ordenesData[key]+'</h3>';
         }
         if(key =='tecnico'){
          var tecnico = ordenesData[key];
         }
         if(key == 'fecha'){
         	var fecha = ordenesData[key];
         }
         if(key == 'piezasCambiadas'){
          var piezasCambiadas = '<p>'+ordenesData[key]+'</p>';
         } 
        }
        post=post+'<br>'+idOT+'<br>'+tecnico+'<br>'+ fecha + '<br>' +piezasCambiadas+'<br>';
       }
      }
    return cursor.continue().then(logItems);
  });