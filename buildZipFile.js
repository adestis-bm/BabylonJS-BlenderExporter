var zipFolder = require('zip-folder');
 
zipFolder('src', './Blender2Babylon-6.1.zip', function(err) {
    if(err) {
        console.log('oh no!', err);
    } else {
        console.log('EXCELLENT');
    }
});