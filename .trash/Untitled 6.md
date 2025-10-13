
schemaVersion: 1.1
description: YAML document from approved VIP
vipInfo:
  vipId: 94A55863E55C49C89A7FFBCCD358A8AF
  name: palazzo-eval
  alternateNames:
  - palazzo-eval.corp.apple.com
  port: 443
  accessLevel: Apple Internal
  protocol: HTTPS
  proxyServerVip: true
  clientIPTransparency: false
  acceptProxyProtocol: false
  vipType: HTTP
  httpVersion: 2.0
  httpRedirectEnabled: true
  environment: PROD
  platform: Data Center
  application: palazzo-comet
  owner: Andreas Schobel
  ownerEmail: aschobel@apple.com
  complianceScope: Not Applicable
  distributionType: Shared
  template: Advanced
  usage: Both
  userTypes:
  - Corporate
  blockVulnerableDevices: true
  shieldServiceTier: Advanced
  dataCenters:
  - name: RENO
    vipDnsName: rn-palazzo-eval-prod.rno.apple.com
    cname:
    - palazzo-eval.corp.apple.com
    pods:
    - name: RNO_INT_SH_POD19
      ipAddress:
      - 10.180.144.42
    - name: RNO_INT_SH_POD20
      ipAddress:
      - 10.180.144.42
  domainName: corp.apple.com
appServerGroups:
- name: default
  https: false
  grpc: false
  excludeRoute: false
  options:
    zone_size: 256k
appServers:
- name: sc0101a-dhcp223.apple.com
  dataCenter: RENO
  pod: ALL
  appServerGroupName: default
  ipAddress: 17.220.14.223
  port: 80
  enabled: true
  useFQDN: false
locations:
- name: default
  path: /
  appServerGroupName: default
  webSocket: false
- name: default_80
  path: /
  webSocket: false
server:
  options:
    add_header:
    - X-Upstream  $upstream_addr
    client_max_body_size: 9999M
    ignore_invalid_headers: "on"
    more_set_headers:
    - '''Strict-Transport-Security max-age=31536000; includeSubdomains'' always'
    - '''X-Frame-Options SAMEORIGIN'' always'
    - '''X-Content-Type-Options nosniff'''
    - '''X-XSS-Protection 1; mode=block'''
    proxy_connect_timeout: 180m
    proxy_http_version: 1.1
    proxy_next_upstream: timeout
    proxy_read_timeout: 180m
    proxy_redirect: "off"
    proxy_request_buffering: "off"
    proxy_send_timeout: 180m
    proxy_set_header:
    - X-Forwarded-For $proxy_add_x_forwarded_for
    - X-Real-IP $realip_remote_addr
    - Connection ""
    - X-Shield-Req-Id $request_id
    - Host $host
    - Proxy ""
    - X-Shield-Vip-Id $vip_id
    - Host $http_host
    - X-Forwarded-Host $http_host
    - X-Forwarded-For $proxy_add_x_forwarded_for
    - X-Forwarded-Proto $http_x_forwarded_proto
    underscores_in_headers: "on"
  accessLogLevel: timed_combined
  errorLogLevel: warn
plugins:
- name: PI_AUTH_DEFAULT_PLUGIN
  pluginName: pi_auth
  appliedToLocations: ALL
  locationNames:
  - default
  - default_80
  options:
    cache: 500k
    enabled: "true"
    primary_timeout: 10
    sec_timeout: 90
ports:
- port: 80
  protocol: HTTP
  options:
    backlog: 1024
    reuseport: ""
- port: 443
  protocol: HTTPS
  options:
    backlog: 1024
    reuseport: ""



schemaVersion: 1.1
description: YAML document from approved VIP
vipInfo:
  vipId: 94A55863E55C49C89A7FFBCCD358A8AF
  name: palazzo-eval
  alternateNames:
  - palazzo-eval.corp.apple.com
  port: 443
  accessLevel: Apple Internal
  protocol: HTTPS
  proxyServerVip: true
  clientIPTransparency: false
  acceptProxyProtocol: false
  vipType: HTTP
  httpVersion: 2.0
  httpRedirectEnabled: true
  environment: PROD
  platform: Data Center
  application: palazzo-comet
  owner: Andreas Schobel
  ownerEmail: aschobel@apple.com
  complianceScope: Not Applicable
  distributionType: Shared
  template: Advanced
  usage: Both
  userTypes:
  - Corporate
  blockVulnerableDevices: true
  shieldServiceTier: Advanced
  dataCenters:
  - name: RENO
    vipDnsName: rn-palazzo-eval-prod.rno.apple.com
    cname:
    - palazzo-eval.corp.apple.com
    pods:
    - name: RNO_INT_SH_POD19
      ipAddress:
      - 10.180.144.42
    - name: RNO_INT_SH_POD20
      ipAddress:
      - 10.180.144.42
  domainName: corp.apple.com
appServerGroups:
- name: default
  https: false
  grpc: false
  excludeRoute: false
  options:
    zone_size: 256k
appServers:
- name: sc0101a-dhcp223.apple.com
  dataCenter: RENO
  pod: ALL
  appServerGroupName: default
  ipAddress: 17.220.14.223
  port: 80
  enabled: true
  useFQDN: false
locations:
- name: default
  path: /
  appServerGroupName: default
  webSocket: false
- name: default_80
  path: /
  webSocket: false
server:
  options:
    client_max_body_size: 9999M
    ignore_invalid_headers: "on"
    more_set_headers:
    - '''Strict-Transport-Security max-age=31536000; includeSubdomains'' always'
    - '''X-Frame-Options SAMEORIGIN'' always'
    - '''X-Content-Type-Options nosniff'''
    - '''X-XSS-Protection 1; mode=block'''
    proxy_connect_timeout: 180m
    proxy_http_version: 1.1
    proxy_next_upstream: timeout
    proxy_read_timeout: 180m
    proxy_redirect: "off"
    proxy_send_timeout: 180m
    proxy_set_header:
    - X-Forwarded-For $proxy_add_x_forwarded_for
    - X-Real-IP $realip_remote_addr
    - Connection ""
    - X-Shield-Req-Id $request_id
    - Host $host
    - Proxy ""
    - X-Shield-Vip-Id $vip_id
    underscores_in_headers: "on"
  accessLogLevel: timed_combined
  errorLogLevel: warn
plugins:
- name: PI_AUTH_DEFAULT_PLUGIN
  pluginName: pi_auth
  appliedToLocations: ALL
  locationNames:
  - default
  - default_80
  options:
    cache: 500k
    enabled: "true"
    primary_timeout: 10
    sec_timeout: 90
ports:
- port: 80
  protocol: HTTP
  options:
    backlog: 1024
    reuseport: ""
- port: 443
  protocol: HTTPS
  options:
    backlog: 1024
    reuseport: ""