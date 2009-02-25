function json(method, url, obj, callback) {
    var xhr = window.ActiveXObject ? new ActiveXObject("Microsoft.XMLHTTP") : new XMLHttpRequest();

    xhr.open(method || 'GET', url, true);
    xhr.setRequestHeader('Content-Type', 'application/json');
    xhr.onreadystatechange = function() {
        if (xhr.readyState == 4) callback(xhr);
    };
    xhr.send(JSON.stringify(obj));
}

function EntryManager(url, common) {
    this.url = url;
    this.common = common;

    this.create = function(entry, opts) {
        for (key in this.common) entry[key] = this.common[key]; 

        json('POST', this.url, entry, function(xml) {
            if (xml.status == 201) {
                if (opts.success) opts.success(JSON.parse(xml.responseText));
            } else {
                if (opts.error) opts.error(xml.statusText);
            }
        });
    };

    this.update = function(entry, opts) {
        json('PUT', this.url + encodeURIComponent(entry.__id__), entry, function(xml) {
            if (xml.status == 200) {
                if (opts.success) opts.success(JSON.parse(xml.responseText));
            } else {
                if (opts.error) opts.error(xml.statusText);
            }
        });
    };

    this.search = function(key, opts) {
        var url = this.url + encodeURIComponent(JSON.stringify(key)) +
                  '?size=' + (opts.size == null ? 10 : opts.size) +
                  '&offset=' + (opts.offset || 0);
        json('GET', url, null, function(xml) {
            if (xml.status == 200) {
                count = parseInt(xml.getResponseHeader("x-items"));
                if (opts.success) opts.success(JSON.parse(xml.responseText), count);
            } else {
                if (opts.error) opts.error(xml.statusText);
            }
        });
    };

    // ``delete`` is a reserved word.
    this.remove = function(id, opts) {
        json('DELETE', this.url + encodeURIComponent(id), null, function(xml) {
            if (xml.status == 204) {
                if (opts.success) opts.success();
            } else {
                if (opts.error) opts.error(xml.statusText);
            }
        });
    };
}
