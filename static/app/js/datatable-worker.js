self.addEventListener("message", function (e) {
    var htmlData = e.data;
    var columns = htmlData.columns;
    var jdata = htmlData.jdata;
    var sdata = [];
    if (htmlData.jobj) {
        columns = [];
        var darr = [];
        var columnData = htmlData.columns;
        for (var k in htmlData.columns) columns.push(k);
        for (var k in htmlData.jdata) darr.push(k);
        for (var i = 0; i < jdata.length; i++) {
            var temp = [];
            if (htmlData.responsive) {
                temp.push("");
            }
            for (var j = 0; j < columns.length; j++) {
                var field = columnData[columns[j]].field;
                if (columnData[columns[j]].normal) {
                    temp.push(jdata[darr[i]].fields[field]);
                }
                if (columnData[columns[j]].editable) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<input id="' + sid + '" name="' + sid + '" type="';
                    if (columnData[columns[j]].password) {
                        stemp += ('password" value="' + jdata[darr[i]].fields[field] + '">');
                    }
                    if (columnData[columns[j]].text) {
                        stemp += ('text" value="' + jdata[darr[i]].fields[field] + '">');
                    }
                    temp.push(stemp);
                }
                if (columnData[columns[j]].link) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<a href="' + jdata[darr[i]].fields[field] + '" id="' + sid + '" name="' + sid + '">' + jdata[darr[i]].fields[field] + '</a>';
                    temp.push(stemp);
                }
                if (columnData[columns[j]].linker) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<a id="' + htmlData.editname + '-' + columns[j] + '" name="' + sid + '">' + field + '</a>';
                    temp.push(stemp);
                }
                if (columnData[columns[j]].switch) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<input class="make-switch" data-size="mini" id="' + htmlData.editname + '-' + columns[j] + '" name="' + sid + '" type="checkbox"';
                    jdata[darr[i]].fields[field] > 0 ? stemp += 'checked />' : stemp += '/>';
                    temp.push(stemp);
                }
                if (columnData[columns[j]].selectable) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<select size="1" id="' + sid + '" name="' + sid + '">';
                    var options = columnData[columns[j]].options;
                    for (var opt in options) {
                        stemp += '<option value="' + options[opt] + '" ';
                        if (jdata[darr[i]].fields[field].toString() === options[opt].toString()) {
                            stemp += 'selected="selected"';
                        }
                        stemp += '>' + opt + '</option>';
                    }
                    temp.push(stemp);
                }
                if (columnData[columns[j]].image) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<img class="img-circle" style="height:39px !important;width:39px !important" id="' + htmlData.editname + '-' + columns[j] + '" name="' + sid + '" src="' + htmlData.baseUrl + '/media/image?pk=' + jdata[darr[i]].fields[field] + '" />';
                    temp.push(stemp);
                }
                if (columnData[columns[j]].multiBtn) {
                    var stemp = "<span>";
                    for (var btn in columnData[columns[j]].order) {
                        var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                        if (columnData[columns[j]].order[btn] === 'starBtn') {
                            stemp += '<button id="' + htmlData.editname + '-active" name="' + sid + '" type="button" class="';
                            if (jdata[darr[i]].fields[field]) {
                                stemp += 'btn btn-success';
                            } else {
                                stemp += 'btn btn-default';
                            }
                            stemp += '"><i class="fa fa-star"></i></button>';

                        }
                        if (columnData[columns[j]].order[btn] === 'editBtn') {
                            stemp += '<button id="' + htmlData.editname + '-edit" name="' + sid + '" type="button" class="btn"><i class="fa fa-pencil"></i></button>';
                        }
                        if (columnData[columns[j]].order[btn] === 'trashBtn') {
                            stemp += '<button id="' + htmlData.editname + '-trash" name="' + sid + '" type="button" href="#confirmDeleteModal" data-toggle="modal" class="btn btn-danger"><i class="fa fa-trash-o"></i></button>';
                        }
                        if (columnData[columns[j]].order[btn] === 'ediHTML') {
                            stemp += '<button id="' + htmlData.editname + '-ediHTML" name="' + sid + '" type="submit" class="btn btn-info"><i class="fa fa-html5"></i></button>';
                        }
                        if (columnData[columns[j]].order[btn] === 'ustreamHTML') {
                            stemp += '<button id="' + htmlData.editname + '-ustreamHTML" name="' + sid + '" type="submit" class="btn btn-info"><i class="fa fa-file"></i></button>';
                        }
                        if (columnData[columns[j]].order[btn] === 'downloadOrig') {
                            stemp += '<button id="' + htmlData.editname + '-download" name="' + sid + '" type="button" class="btn btn-info"><i class="fa fa-download"></i></button>';
                        }
                    }
                    stemp += "</span>";
                    temp.push(stemp);
                }
                if (columnData[columns[j]].rating) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<select id="' + sid + '" name="' + sid + '" type="">';
                    stemp += '<option value=""></option>';
                    for (var starCount = 1; starCount <= 10; starCount++) {
                        stemp += '<option value="' + starCount + '">' + starCount + '</option>';
                    }
                    stemp += '</select>';
                    temp.push(stemp);
                }
                if (columnData[columns[j]].download) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<button id="' + htmlData.editname + '-download" name="' + sid + '" type="button" class="btn btn-info"><i class="fa fa-download"></i></button>';
                    temp.push(stemp);
                }
                if (columnData[columns[j]].starBtn) {
                    var stemp = '<button id="' + htmlData.editname + '-active" type="button" class="';
                    if (jdata[darr[i]].fields[field]) {
                        stemp += 'btn btn-success';
                    } else {
                        stemp += 'btn btn-default';
                    }
                    stemp += '"><i class="fa fa-star"></i></button>';
                    temp.push(stemp);
                }
                if (columnData[columns[j]].trashBtn) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<button id="' + htmlData.editname + '-trash" name="' + sid + '" type="button" href="#confirmDeleteModal" data-toggle="modal" class="btn btn-danger"><i class="fa fa-trash-o"></i></button>';
                    temp.push(stemp);
                }
                if (columnData[columns[j]].selectablelist) {
                    var options = columnData[columns[j]].options;
                    for (var opt in options) {
                        if (jdata[darr[i]].fields[field].toString() === options[opt].toString()) {
                            temp.push(opt);
                        }
                    }
                }
                if (columnData[columns[j]].postNoteBtn) {
                    var sid = htmlData.editname + '-' + jdata[darr[i]].pk + '-' + columns[j];
                    var stemp = '<button type="button" class="btn btn-circle blue btn-sm" data-toggle="modal" href="#postModal" id=' + htmlData.editname + '-' + columns[j] + '" name="' + sid + '"> Notes </button>';
                    temp.push(stemp);
                }
            }
            sdata.push(temp);
        }
        postMessage(sdata);
    } else {
        for (var i = 0; i < jdata.length; i++) {
            var temp = [];
            if (htmlData.responsive) {
                temp.push("");
            }
            for (var j = 0; j < columns.length; j++) {
                if (columns[j] === 'wiki') {
                    temp.push('<a id="wiki">Wiki Page</a>');
                } else {
                    temp.push(jdata[i].fields[columns[j]]);
                }

            }
            sdata.push(temp);
        }
        postMessage(sdata);
    }
}, false);