import datetime

def generate_error_msg(mgr_name, err):
    if hasattr(err, 'parent') and hasattr(err.parent, 'message'):
        if 'Conversion failed' in err.parent.message:
            err.message = "Invalid data type"

        if 'duplicate key' in err.parent.message:
            err.message = "Required Unique Data"

        if 'Invalid column name' in err.parent.message:
            err.message = "Invalid Column"

        if 'Unclosed quotation mark' in err.parent.message or 'Incorrect syntax near' in err.parent.message:
            err.message = "Invalid Query"

        print({"Time:": datetime.datetime.now().isoformat(), 'MgrName': mgr_name, 'error': err.parent.message, 'sql': err.parent.sql})
    else:
        print({"Time:": datetime.datetime.now().isoformat(), 'MgrName': mgr_name, 'error': err})

    return err
