# Mayflower MicroK8s Addon Repository

This is our repository for MicroK8s addons we like to use. Obviously we would like to transfer them to the official [MicroK8s Community Repository](https://github.com/canonical/microk8s-community-addons/) when they are in a proper state, including tests and documentation. 
Please regard this repository as development only, all mature software is going to be moved to the community repository. 

This repository contains 10 addons:

* **spin**, a framework for building and running event-driven microservice applications with WebAssembly
* **istio**, a copy of the existing plugin with an updated version 
* **redis**, a simple redis addon based on bitnamis helm chart, needed for dapr
* **dapr**, a platform agnostic event driven application runtime for microservices
* **kubevela**, an application centric sofftware delivery platform based on the OAM standard
* **keycloak**, a service for user federation, strong authentication, user management, fine-grained authorizatio
* **kubeview**, a Kubernetes cluster visualiser and visual explorer
* **postgresql**, an open source object-relational database known for reliability and data integrity
* **nocalhost**, a cloud-native development tool with integrated IDE support
* **buildkit**, a tool for building container images with your Kubernetes cluster

## Addons

To use the addons provided by this repository please add it to your current microk8s setup:

```
microk8s addons repo add mayflower https://github.com/mayflower/microk8s-addons/
```

<<<<<<< HEAD

=======
>>>>>>> dbd673a (A bit more documentation)
### Nocalhost

This addon provides support for (Nocalhost)[https://nocalhost/]

> Nocalhost is an open-source IDE plugin for cloud-native applications development:
> 
> * Build, test and debug applications directly inside Kubernetes
> 
> * IDE Support : providing the same debugging and developing experience you're used in the IDE even in the remote Kubernetes cluster
> 
> * Developing with instant file synchronization: instantly sync your code change to remote container without rebuilding images or restarting containers.

This addon installs nocalhost into your microk8s cluster and provides the nhctl command line Interface. 

<<<<<<< HEAD

### Buildkit

This addon installs support for [BuildKit CLI](https://github.com/vmware-tanzu/buildkit-cli-for-kubectl)

> BuildKit CLI for kubectl is a tool for building OCI and Docker images with your kubernetes cluster. 
> It replaces the docker build command to let you quickly and easily build your single and 
> multi-architecture container images.

To enable BuildKit CLI support type
```
microk8s enable buildkit
```
Now two additional commands are available: 
```
microk8s kubectl build
microk8s kubectl buildkit
```


=======
>>>>>>> dbd673a (A bit more documentation)
### Spin / Wasm Addon

This addon installs support for [Spin](https://spin.fermyon.dev/)

> Spin is a framework for building and running event-driven microservice applications with
> WebAssembly (Wasm) components. With Spin, we’re trying to make it easier to get started 
> with using WebAssembly on the server so that we can all take advantage of the security, 
> portability, and speed WebAssembly provides when it comes to running microservices.    

This addon provides a simple way to make your first steps with web assembly payloads. 

You can enable Spin support with 

```
microk8s enable spin
```

The spin module includes a wrapper for [wasm-to-oci](https://github.com/engineerd/wasm-to-oci), that can be used 
to push WebAssembly modules to the microk8s registry: 

```
microk8s enable registry 
microk8s wasm-to-oci push ./spin_hello_world.wasm localhost:32000/spin-hello-world:registry
```

### KeyCloak Addon

This addon installs [KeyCloak](https://www.keycloak.org/)

> Add authentication to applications and secure services with minimum effort.
> No need to deal with storing users or authenticating users.
> Keycloak provides user federation, strong authentication, user management, fine-grained authorization, and more.

This addon provides a simple way to use KeyClak within your microk8s setup.

You can enable Keycloak support with:

```
microk8s enable mayflower/keycloak
```

Please note that this addon is based on the bitnami helm chart and supports a number of additional parameters that can be found [here](https://artifacthub.io/packages/helm/bitnami/keycloak):

```
microk8s enable mayflower/keycloak --set  --set auth.adminPassword=secretpassword
```

### The Redis Addon

This addon installs [Redis](https://redis.io/):

> The open source, in-memory data store used by millions of developers as a database, cache, streaming engine, and message broker. 

This addon is meant as a support for the dapr addon, that relies on redis as state and configuration storage as well as message broker. 
However, it can be used on its own whenevery you need redis within your microk8s setup. 
You can enable Redis support with:

```
microk8s enable mayflower/redis
```

Please note that this addon is based on the bitnami helm chart and supports a number of additional parameters that can be found [here](https://artifacthub.io/packages/helm/bitnami/redis):

```
microk8s enable mayflower/redis --set auth.password=secretpassword
```

### The PostgreSQL Addon

This addon installs [PostgreSQL](https://www.postgresql.org/):

> PostgreSQL is a powerful, open source object-relational database system with over 30 years of active development that has earned it a strong reputation for reliability, feature robustness, and performance.

This addon provides a simple way to provide a PostgreSQL database within your microk8s setup.

You can enable postgresql support with:

```
microk8s enable postgresql
```

Please note that this addon is based on the bitnami helm chart and supports a number of additional parameters that can be found [here](https://artifacthub.io/packages/helm/bitnami/postgresql):

```
microk8s enable mayflower/postgresql --set auth.postgresPassword=secretpassword
```

### KubeView Addon

This addon installs [KubeView](https://kubeview.benco.io/):

> KubeView displays what is happening inside a Kubernetes cluster (or single namespace), it maps out the API objects and how they are interconnected. Data is fetched real-time from the Kubernetes API. The status of some objects (Pods, ReplicaSets, Deployments) is colour coded red/green to represent their status and health

This addon provides a nice overview what is going on in your microk8s.

You can enable postgresql support with:

```
microk8s enable kubeview
```

Please note that this addon is based on the official helm chart and supports a number of additional parameters that can be found [here](https://kubeview.benco.io/):

```
microk8s enable mayflower/kubeview --set ingress.enabled=true
```

### The Istio Addon

This addon installs [Istio](https://istio.io):

> Istio extends Kubernetes to establish a programmable, application-aware network using the powerful Envoy service proxy. Working with both Kubernetes and traditional workloads, Istio brings standard, universal traffic management, telemetry, and security to complex deployments.

You can enable Istio support with:

```
microk8s enable mayflower/istio
```

This addon uses the command line client istioctl to install Istio. 
It is provided as a plugin within microk8s and can be used for administration tasks:

```
microk8s istioctl verify-install
```

### The Dapr Addon

This addon installs https://dapr.io/:

> The Distributed Application Runtime (Dapr) provides APIs that simplify microservice connectivity. Whether your communication pattern is service to service invocation or pub/sub messaging, Dapr helps you write resilient and secured microservices.
> By letting Dapr’s sidecar take care of the complex challenges such as service discovery, message broker integration, encryption, observability, and secret management, you can focus on business logic and keep your code simple.

It provides a simple dapr setup including state management, publish and subscribe messaging and configuration management based on the redis addon. 

You can enable Dapr support with:

```
microk8s enable dapr 
```

This addon installs the dapr command line client as a MicroK8s plugin. 

```
microk8s dapr
```

The Dapr Addon automatically installs the redis addon and configures it as a statestore, a configstore and pubsub component for dapr in microk8s. 

#### Dapr Example

This example uses the [Dapr hello-kubernetes quickstart](https://github.com/dapr/quickstarts/tree/master/tutorials/hello-kubernetes) provided by dapr here. 

Clone the repository and cd into the kubernetes example: 

```
git clone https://github.com/dapr/quickstarts.git
cd quickstarts/tutorials/hello-kubernetes
```

#### Deploy the Node.js app with the Dapr sidecar

```shell
microk8s kubectl apply -f ./deploy/node.yaml
```

Kubernetes deployments are asyncronous. This means you'll need to wait for the deployment to complete before moving on to the next steps. You can do so with the following command:

```shell
microk8s kubectl rollout status deploy/nodeapp
```

This will deploy the Node.js app to Kubernetes. The Dapr control plane will automatically inject the Dapr sidecar to the Pod. If you take a look at the `node.yaml` file, you will see how Dapr is enabled for that deployment:

`dapr.io/enabled: true` - this tells the Dapr control plane to inject a sidecar to this deployment.

`dapr.io/app-id: nodeapp` - this assigns a unique id or name to the Dapr application, so it can be sent messages to and communicated with by other Dapr apps.

`dapr.io/enable-api-logging: "true"` - this is added to node.yaml file by default to see the API logs.

#### Verify Service

You can check the service using a port forward.

```shell
microk8s kubectl port-forward service/nodeapp 8080:80
```

This will make your service available on [http://localhost:8080](http://localhost:8080/).

To call the service that you set up port forwarding to, from a command prompt run:

```shell
curl http://localhost:8080/ports
```

Expected output:

```
{"DAPR_HTTP_PORT":"3500","DAPR_GRPC_PORT":"50001"}
```

Next submit an order to the app

```shell
curl --request POST --data "@sample.json" --header Content-Type:application/json http://localhost:8080/neworder
```

Expected output: Empty reply from server

Confirm the order was persisted by requesting it from the app

```shell
curl http://localhost:8080/order
```

Expected output:

```json
{ "orderId": "42" }
```

#### Dapr Dashboard

Dapr provides a dashboard as a convenient interface to check status, information and logs of applications running on Dapr. The following command will make it available on [http://localhost:9999/](http://localhost:9999/).

```shell
microk8s dapr dashboard -k -p 9999
```

#### Deploy the Python app with the Dapr Sidecar

Next, take a quick look at the Python app. Navigate to the Python app in the kubernetes quickstart: `cd quickstarts/tutorials/hello-kubernetes/python` and open `app.py`.

At a quick glance, this is a basic Python app that posts JSON messages to `localhost:3500`, which is the default listening port for Dapr. You can invoke the Node.js application's `neworder` endpoint by posting to `v1.0/invoke/nodeapp/method/neworder`. The message contains some `data` with an orderId that increments once per second:

```python
n = 0
while True:    n += 1
    message = {"data": {"orderId": n}}    try:        response = requests.post(dapr_url, json=message)    except Exception as e:        print(e)    time.sleep(1)
```

Deploy the Python app to your Kubernetes cluster:

```shell
microk8s kubectl apply -f ./deploy/python.yaml
```

As with above, the following command will wait for the deployment to complete:

```shell
microk8s kubectl rollout status deploy/pythonapp
```

#### Observe Messages

Get the logs of the Node.js app:

```shell
microk8s kubectl logs --selector=app=node -c node --tail=-1
```

If all went well, you should see logs like this:

```
Got a new order! Order ID: 1
Successfully persisted state
Got a new order! Order ID: 2
Successfully persisted state
Got a new order! Order ID: 3
Successfully persisted state
```

Get the API call logs of the Python app:

```shell
microk8s kubectl logs --selector=app=python -c daprd --tail=-1
```

```
time="2022-04-27T02:47:49.972688145Z" level=info msg="HTTP API Called: POST /neworder" app_id=pythonapp instance=pythonapp-545df48d55-jvj52 scope=dapr.runtime.http-info type=log ver=1.7.2
time="2022-04-27T02:47:50.984994545Z" level=info msg="HTTP API Called: POST /neworder" app_id=pythonapp instance=pythonapp-545df48d55-jvj52 scope=dapr.runtime.http-info type=log ver=1.7.2
```

#### Confirm successful persistence

Call the Node.js app's order endpoint to get the latest order. Grab the external IP address that you saved before and, append "/order" and perform a GET request against it (enter it into your browser, use Postman, or curl it!):

```
curl http://localhost:8080/order
{"orderID":"42"}
```

You should see the latest JSON in response!

### The KubeVela Addon

This addon installs [KubeVela](https://kubevela.io):

> KubeVela is a modern software delivery platform that makes deploying and operating applications across today's hybrid, multi-cloud environments easier, faster and more reliable.
> KubeVela is infrastructure agnostic, programmable, yet most importantly, application-centric. It allows you to build powerful software, and deliver them anywhere!

It provides KubeVela with VelaUX (the web ui for KubeVela).

You can enable KubeVela support with:

```
microk8s enable kubevela
```

This addon install the vela command line client as a microk8s plugin.

```
microk8s vela version
```

<<<<<<< HEAD
Vela can be used with the velaux dashboard. 

```shell
 microk8s vela port-forward -n vela-system addon-velaux 9082:80
```



## How to use this addons repository

=======
## How to use this addons repository

>>>>>>> dbd673a (A bit more documentation)
### Adding repositories

3rd party addons repositories are supported on MicroK8s v1.24 and onwards. To add a repository on an already installed MicroK8s you have to use the `microk8s addons repo` command and provide a user friendly repo name, the path to the repository and optionally a branch within the repository. For this repository:

```
microk8s addons repo add mayflower https://github.com/mayflower/microk8s-addons/ --reference main
```

### Enabling/disabling addons

The addons of all repositories are shown in `microk8s status` along with the repo they came from. `microk8s enable` and `microk8s disable` are used to enable and disable the addons respectively. The repo name can be used to disambiguate between addons with the same name. For example:

```
microk8s enable mayflower/redis
```

### Refreshing repositories

Adding a repository to MicroK8s (via `microk8s addons repo add`) creates a copy of the repository under `$SNAP_COMMON/addons` (typically under `/var/snap/microk8s/common/addons/`). Authorized users are able to edit the addons to match their need. In case the upstream repository changes and you need to pull in any updates with:

```
microk8s addons repo update mayflower
```

### Removing repositories

Removing repositories is done with:

```
microk8s addons repo remove mayflower
```

## Repository structure

An addons repository has the following structure:

```
addons.yaml         Authoritative list of addons included in this repository. See format below.
addons/
    <addon1>/
        enable      Executable script that runs when enabling the addon
        disable     Executable script that runs when disabling the addon
    <addon2>/
        enable
        disable
    ...
```

At the root of the addons repository the `addons.yaml` file lists all the addons included. This file is of the following format:

```yaml
microk8s-addons:
  # A short description for the addons in this repository.
  description: Core addons of the MicroK8s project

  # Revision number. Increment when there are important changes.
  revision: 1

  # List of addons.
  addons:
    - name: addon1
      description: My awesome addon

      # Addon version.
      version: "1.0.0"

      # Test to check that addon has been enabled. This may be:
      # - A path to a file. For example, "${SNAP_DATA}/var/lock/myaddon.enabled"
      # - A Kubernetes resource, in the form `resourceType/resourceName`, just
      #   as it would appear in the output of the `kubectl get all -A` command.
      #   For example, "deployment.apps/registry".
      #
      # The addon is assumed to be enabled when the specified file or Kubernetes
      # resource exists.
      check_status: "deployment.apps/addon1"

      # List of architectures supported by this addon.
      # MicroK8s supports "amd64", "arm64" and "s390x".
      supported_architectures:
        - amd64
        - arm64
        - s390x

    - name: addon2
      description: My second awesome addon, supported for amd64 only
      version: "1.0.0"
      check_status: "pod/addon2"
      supported_architectures:
        - amd64
```

## Adding new addons

See [`HACKING.md`](./HACKING.md) for instructions on how to develop custom MicroK8s addons.
