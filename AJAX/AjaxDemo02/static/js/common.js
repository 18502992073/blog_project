/**
 * Created by tarena on 19-5-31.
 */
function createXhr() {
    if (window.XMLHttpRequest){
        return new XMLHttpRequest();
    }else {
        return new ActiveXObject("Micorsoft.XMLHTTP");
    }
}

