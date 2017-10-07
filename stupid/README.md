# Client library

In this directory is a python library for communicating with the parking server. Since each individual sensor package is a node in the parking network, this is the "Node" library.

## Config

The library is configured using a `config.json` file. This file contains:

* `server` (required) - the address of the parking server
* `lot` (optional) - specify an initial parking lot id on registration
* `lock` (optional, defaults to `True`) - should this node's registration be persistent? (see below)
* `key` (optional) - overrides this node's registration key

## Lock

The lock file is used to make registrations persistent, so that a node won't have to re-register with the server every time it starts. It can contain all the same data as `config.json`. However, instead of being user-specified, `lock.json` is provided by the server,

## Connect

The main function in the library is the `connect` function. The connect function combines any passed, parameters, the config file, and the lock file. If there is no registration key present, it also registers with the provided server and saves the response in `lock.json`.

1. `kwargs`
2. `config.json`
3. `GET \register` response (if `key` is absent from other sources)
4. `lock.json` (if used)

## Node

To use the `Node` class:
1. Update `Node.enter`, `Node.exit`, or call `Node.delta()`
2. `Node.send_report()`
