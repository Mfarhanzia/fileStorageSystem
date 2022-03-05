$(document).ready(function() {
    (async function () {
        const response = await getFolders()
        const folderRows = $("tbody#folders")
        updateTableRows(folderRows, response)
        $(document).find("tbody#folders td").on("click", function(){
            folderRows.find("td").removeClass('active')
            $(this).addClass('active')
            getDocuments(this.getAttribute("obj_id"))
        })
        getFilterTopics()
    })();

    function getFolders() {
        return $.ajax({
            type: 'GET',
            url: 'api/v1/filesystem/folders',
            success: function(response) {
                return response
            }
        });
    }

    function getDocuments(folderId){
        const queryParams = {}
        if (folderId)
            queryParams["folder_id"] = folderId
        $("#topicFilterSelect").val()
        const topicsValues = $("#topicFilterSelect").val()
        if (topicsValues){
           queryParams["topics"] = topicsValues
        }
        $.ajax({
            type: 'GET',
            data: queryParams,
            url: 'api/v1/filesystem/documents',
            success: function(response) {
                const documentRows = $("tbody#documents")
                documentRows.empty()
                updateTableRows(documentRows, response)
                return response
            }
        });
    }

    function updateTableRows(element, response){
        if (response){
            $.map(response, function(obj){
                element.append(`
                    <tr>
                        <td class="cursor" obj_id="${obj.id}">
                            ${obj.file ? 
                                `<a target="_blank" href="${obj.file}">${obj.name}</a>` 
                            : obj.title}
                        </td>
                    </tr>
                `);
            })
        }else{
            element.append(`
                <tr>
                    <td>empty</td>
                </tr>
            `);
        }
    }

    $("form#addFolderForm").on("submit",function (e){
        e.preventDefault()
        const data = $(this).serializeArray()
        const csrfToken = $("input[name=csrfmiddlewaretoken]").val()
        data.push({ name: "csrfmiddlewaretoken", value: csrfToken });
        $.ajax({
            type: 'POST',
            data: data,
            url: 'api/v1/filesystem/folders',
            success: function(response) {
                $("form#addFolderForm input").val("")
                const folderRows = $("tbody#folders")
                updateTableRows(folderRows, [response])
                return response
            },
            error: function (request, status, error) {
                alert(request.responseJSON.title[0]);
            }
        });
    })

    $("form#addTopicForm").on("submit",function (e){
        e.preventDefault()
        const data = $(this).serializeArray()
        const csrfToken = $("input[name=csrfmiddlewaretoken]").val()
        data.push({ name: "csrfmiddlewaretoken", value: csrfToken });
        $.ajax({
            type: 'POST',
            data: data,
            url: 'api/v1/filesystem/topics',
            success: function(response) {
                $("form#addTopicForm input").val("")
                getFilterTopics()
                return true
            },
            error: function (request, status, error) {
                alert(request.responseJSON.title[0]);
            }
        });
    })

    async function updateSelectFolders(){
        const response = await getFolders()
        const folderSelect = $("select#folderSelect")
        folderSelect.empty()
        updateOptions(folderSelect, response)
    }

    function getTopics(){
        $.ajax({
            type: 'GET',
            url: 'api/v1/filesystem/topics',
            success: function(response) {
                const topicSelect = $("select#topicSelect")
                topicSelect.empty()
                updateOptions(topicSelect, response)
                return true
            },
            error: function (request, status, error) {
                alert(request.responseText);
            }
        });
    }

    function updateOptions(element, response){
        if (response){
            $.map(response, function(obj){
                element.append(`<option value="${obj.id}">${obj.title}</option>`);
            })
        }else{
            element.append(`<option disabled>Empty</option>`);
        }
    }

    $('#UploadDocumentModal').on('show.bs.modal', function () {
        updateSelectFolders()
        getTopics()
    })

    $("form#uploadDocument").on("submit",function (e){
        e.preventDefault()
        const csrfToken = $("input[name=csrfmiddlewaretoken]").val()
        const formData = new FormData(this)
        // formData.append("csrfmiddlewaretoken", csrfToken)
        // formData.append("file", uploadedFile, uploadedFile.name)
        $.ajax({
            type: 'POST',
            processData: false,
            contentType: false,
            url: 'api/v1/filesystem/documents',
            data: formData,
            success: function(response) {
                $('#UploadDocumentModal').modal("hide")
            },
            error: function (request, status, error) {
                alert(request.responseText);
            }
        });
    })

    function getFilterTopics(){
        $.ajax({
            type: 'GET',
            url: 'api/v1/filesystem/topics',
            success: function(response) {
                const topicSelect = $("select#topicFilterSelect")
                topicSelect.empty()
                updateOptions(topicSelect, response)
                return true
            },
            error: function (request, status, error) {
                alert(request.responseText);
            }
        });
    }
});