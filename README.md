## Mayflower MicroK8s Addon Repository

This is our repository for MicroK8s addons we like to use. Obviously we would like to transfer them to the official [MicroK8s Community Repository](https://github.com/canonical/microk8s-community-addons/) when they are in a proper state, including tests and documentation. 
Please regard this repository as development only, all mature software is going to be moved to the community repository. 

This repository contains 4 addons:

  * istio, a copy of the existing plugin with an updated version 
  * redis, a simple redis addon based on bitnamis helm chart, needed for dapr
  * dapr, a platform agnostic event driven application runtime for microservices
  * kubevela, an application centric sofftware delivery platform based on the OAM standard

All addons should work on amd64 and arm64 architectures.

### Addons

To use the addons provided by this repository please add it to your current microk8s setup:
```
microk8s addons repo add mayflower https://github.com/mayflower/microk8s-addons/
```

#### The Redis Addon

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

#### The PostgreSQL Addon

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

#### KubeView Addon


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



#### The Istio Addon

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
#### The Dapr Addon

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
microk8s dapr version
```

#### The KubeVela Addon

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


### How to use this addons repository

#### Adding repositories
3rd party addons repositories are supported on MicroK8s v1.24 and onwards. To add a repository on an already installed MicroK8s you have to use the `microk8s addons repo` command and provide a user friendly repo name, the path to the repository and optionally a branch within the repository. For this repository:
```
microk8s addons repo add mayflower https://github.com/mayflower/microk8s-addons/ --reference main
```

#### Enabling/disabling addons

The addons of all repositories are shown in `microk8s status` along with the repo they came from. `microk8s enable` and `microk8s disable` are used to enable and disable the addons respectively. The repo name can be used to disambiguate between addons with the same name. For example:

```
microk8s enable mayflower/redis
```


#### Refreshing repositories

Adding a repository to MicroK8s (via `mcirok8s addons repo add`) creates a copy of the repository under `$SNAP_COMMON/addons` (typically under `/var/snap/microk8s/common/addons/`). Authorized users are able to edit the addons to match their need. In case the upstream repository changes and you need to pull in any updates with:
```
microk8s addons repo update mayflower
```

#### Removing repositories

Removing repositories is done with:
```
microk8s addons repo remove mayflower
```


### Repository structure

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
