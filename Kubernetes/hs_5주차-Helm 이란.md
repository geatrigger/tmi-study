# Helm 이란

[Helm 개념과 구조 기술조사](https://lifeplan-b.tistory.com/m/35?category=828034)

**Helm 이란?**

- Kubernetes 의
    
    **패키지 관리 도구**
    
- Linux의 Yum, Apt와 비슷한 형태로 Kubernetes 패키지 배포를 가능하게 해주는 Tool
- 어플리케이션을 패키징하여 Kubernetes Cluster에 배포할 수 있도록 도와줌

**Helm을 사용하는 이유?**

**어플리케이션 배포 + 필요한 Kubernetes 리소스까지 모두 배포해주는 역할을 한다.**

일반적으로 하나의 소프트웨어 or 어플리케이션을 배포하는데, 하나의 컨테이너만으로 해결되는 경우는 적다.

Ingress, Service, Pod, 디스크 볼륨, 기타 정책까지 추가적으로 배포해야 한다.

따라서, 하나의 어플리케이션을 위해서 많은 구성 및 설정이 필요해서 복잡해지는데,

이러한 하나의 소프트웨어를 배포하기 위해 필요한 모든 설정, 리소스의 배포를 패키지 형태로 지원한다.

담당자가 변경되었을때 or 새로운 매니페스트를 적용해야 할때 or 다른 쿠버네티스 클러스터로 이동될때

개별 매니페스트를 모두 개별 조정해줄것이 아니라. Helm의 표준 형식에 조정이 필요한 설정 과 변수만 조정하여 사용자가 쉽게 어플리케이션 설치를 할 수 있다.

**Helm 을 통한 쿠버네티스 위에 엘라스틱서치 올리기**

[Install Elasticsearch on Kubernetes via Helm Chart | phoenixNAP KB](https://phoenixnap.com/kb/elasticsearch-helm-chart)

Helm install

[Installing Helm](https://helm.sh/docs/intro/install/)

```jsx
curl https://baltocdn.com/helm/signing.asc | sudo apt-key add -
sudo apt-get install apt-transport-https --yes
echo "deb https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

```jsx
helm repo add elastic https://helm.elastic.co
curl -O https://raw.githubusercontent.com/elastic/helm-charts/master/elasticsearch/examples/minikube/values.yaml
```