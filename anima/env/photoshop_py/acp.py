import os
import socket
import traceback


def send(cmd, port):

    host = '127.0.0.1'

    # we expect a result no matter if it errors, so we keep trying until we
    # get a reply. This is slow, but relyable.
    keep_trying = True
    result = ""
    while(keep_trying):
        conn = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        conn.connect((host, port))
        conn.send(cmd)
        try:
            result = conn.recv(4096)
            conn.close()
            if result:
                keep_trying = False
        except:
            pass

    # raise error
    if result.startswith("Error: "):
        msg = result.replace("Error: ", "")
        msg += "CMD: " + cmd
        raise ValueError(msg)

    # all replies comes in with a newline
    result = result.replace("\n", "")

    # more Pythonic return of nothing
    if result == "undefined":
        return None

    return result


def stop_server(port):
    send("keep_serving = false", port)


if __name__ == '__main__':
    port = int(os.environ["AFTEREFFECTS_PORT"])
    try:
        # Experiment with sending Javascipt commands here safely.
        print "Photoshop version: {0}".format(
            send("return app.version", port)
        )
    except:
        print traceback.format_exc()
    finally:
        raw_input("Pause... Press any key to continue")
        stop_server(port)
