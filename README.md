**Flask 기반 API 코드, 클라이언트가 제공한 주소들을 Geopy로 위도와 경도를 얻고, 이를 Folium을 사용해 지도에 동적으로 표시하는 웹 애플리케이션**

**주요 기능**
- **Geopy**와 **Folium**을 이용한 **동적 지도 시각화**:
  - 주소를 위도, 경도로 변환하고, Folium을 통해 지도에 마커를 동적으로 표시
  - 요청된 주소에 대해 **상점 위치**를 **지도에 시각화**
  - 선택된 주소는 빨간 마커로 강조

### 의존성 파일
`geo_api.txt`

### Docker 파일
`Dockerfile.geo`

**웹 페이지는 별도로 만들어 사용** => `https://github.com/project-3-payday-SKshieldus/payday_react`

## API 엔드포인트
### `POST /geo`
- 주소 리스트를 받아 Geopy로 위도와 경도를 계산하고, Folium을 이용해 지도에 마커를 표시

**요청 예시**
```json
{
  "addresses": ["서울특별시 강서구 공항대로 247"],
  "storeNames": ["Store 1"],
  "selectedIndex": 0
}
```
