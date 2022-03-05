import uuid


def document_upload_path(instance, filename):
    """
    helper function to add unique identifier to file name
    """
    folder_name = "other"
    if instance.folder:
        folder_name = instance.folder.title
    return '{}/{}--{}'.format(folder_name, str(uuid.uuid4()), filename)
