import sh
import yaml

from utils import microk8s_enable, wait_for_pod_state, microk8s_disable


class TestAddons(object):
    def test_dapr(self):
        microk8s_enable("dapr")
        wait_for_pod_state("", "dapr-system", "running", label="app=dapr-dashboard")
        status = yaml.safe_load(sh.microk8s.status(format="yaml").stdout)
        expected = {"dapr": "enabled"}
        microk8s_disable("dapr")

    def test_kubevela(self):
        microk8s_enable("kubevela")
        wait_for_pod_state("", "vela-system", "running", label="app.kubernetes.io/instance=kubevela")
        status = yaml.safe_load(sh.microk8s.status(format="yaml").stdout)
        expected = {"kubevela": "enabled"}
        microk8s_disable("kubevela")
