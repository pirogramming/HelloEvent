// 주소-좌표 변환 객체를 생성합니다
var geocoder = new kakao.maps.services.Geocoder();
var mapContainer = document.getElementById("map"), // 지도를 표시할 div
  mapOption = {
    center: new kakao.maps.LatLng(33.450701, 126.570667), // 지도의 중심좌표
    level: 5, // 지도의 확대 레벨
  };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

//유저가 등록한 선호 장소로 맵이 바로 나타나게 함
findUserPreferLocation();

var map_infowindow = new kakao.maps.InfoWindow({ zindex: 1 }); // 클릭한 위치에 대한 주소를 표시할 인포윈도우입니다

// // 현재 지도 중심좌표로 주소를 검색해서 지도 좌측 상단에 표시합니다
// searchAddrFromCoords(map.getCenter(), displayCenterInfo);

// 지도에 표시된 마커 객체를 가지고 있을 배열입니다
var markers = [];

let changed_coordinate;
// 지도를 클릭한 위치에 표출할 마커입니다
var marker = new kakao.maps.Marker();
marker.setMap(map);

// 지도에 클릭 이벤트를 등록합니다
// 지도를 클릭하면 마지막 파라미터로 넘어온 함수를 호출합니다
kakao.maps.event.addListener(map, "click", function (mouseEvent) {
  // 클릭한 위도, 경도 정보를 가져옵니다
  var latlng = mouseEvent.latLng;

  searchDetailAddrFromCoords(mouseEvent.latLng, function (result, status) {
    if (status === kakao.maps.services.Status.OK) {
      var detailAddr = !!result[0].road_address
        ? "<div>도로명주소 : " + result[0].road_address.address_name + "</div>"
        : "";
      detailAddr +=
        "<div>지번 주소 : " + result[0].address.address_name + "</div>";

      // 도시, 구까지 파싱하고 나머지 주소 파싱 과정
      let restAddr = result[0].address.address_name.split(" ");
      // 파싱한 도시 이름
      let cityName = restAddr[0];
      // 파싱한 구 이름
      let guName = restAddr[1];
      restAddr = restAddr.filter(
        (address) =>
          restAddr.indexOf(address) != 0 && restAddr.indexOf(address) != 1
      );

      //최종 restAddr = 도시, 구를 제외한 나머지 주소
      restAddr = restAddr.join(" ");
      console.log(cityName, guName, restAddr);

      var content =
        '<div class="bAddr" style="padding:5px;text-overflow: ellipsis;overflow: hidden;white-space: nowrap;">' +
        '<span class="title">법정동 주소정보</span>' +
        detailAddr +
        "</div>";

      // 마커를 클릭한 위치에 표시합니다
      marker.setPosition(mouseEvent.latLng);
      marker.setMap(map);

      // 인포윈도우에 클릭한 위치에 대한 법정동 상세 주소정보를 표시합니다
      map_infowindow.setContent(content);
      map_infowindow.open(map, marker);
    }
  });

  // 마커 위치를 클릭한 위치로 옮깁니다
  // marker.setPosition(latlng);
  addMarker(latlng);
  hideMarkers();

  changed_coordinate = [latlng.getLat(), latlng.getLng()];
  var message = "클릭한 위치의 위도는 " + latlng.getLat() + " 이고, ";
  message += "경도는 " + latlng.getLng() + " 입니다";
  panTo();
  console.log(message);
});

function searchAddrFromCoords(coords, callback) {
  // 좌표로 행정동 주소 정보를 요청합니다
  geocoder.coord2RegionCode(coords.getLng(), coords.getLat(), callback);
}

function searchDetailAddrFromCoords(coords, callback) {
  // 좌표로 법정동 상세 주소 정보를 요청합니다
  geocoder.coord2Address(coords.getLng(), coords.getLat(), callback);
}

// 지도 좌측상단에 지도 중심좌표에 대한 주소정보를 표출하는 함수입니다
function displayCenterInfo(result, status) {
  if (status === kakao.maps.services.Status.OK) {
    var infoDiv = document.getElementById("centerAddr");

    for (var i = 0; i < result.length; i++) {
      // 행정동의 region_type 값은 'H' 이므로
      if (result[i].region_type === "H") {
        infoDiv.innerHTML = result[i].address_name;
        break;
      }
    }
  }
}

// 중심 좌표나 확대 수준이 변경됐을 때 지도 중심 좌표에 대한 주소 정보를 표시하도록 이벤트를 등록합니다
kakao.maps.event.addListener(map, "idle", function () {
  searchAddrFromCoords(map.getCenter(), displayCenterInfo);
});

// 마커를 생성하고 지도위에 표시하는 함수입니다
function addMarker(position) {
  // 마커를 생성합니다
  var marker = new kakao.maps.Marker({
    position: position,
  });

  // 마커가 지도 위에 표시되도록 설정합니다
  marker.setMap(map);

  // 생성된 마커를 배열에 추가합니다
  markers.push(marker);
}

// 배열에 추가된 마커들을 지도에 표시하거나 삭제하는 함수입니다
function setMarkers(map) {
  for (var i = 0; i < markers.length - 1; i++) {
    markers[i].setMap(map);
  }
}

// "마커 감추기" 버튼을 클릭하면 호출되어 배열에 추가된 마커를 지도에서 삭제하는 함수입니다
function hideMarkers() {
  setMarkers(null);
}

// 지도 중심을 자연스럽게 옮겨주는 함수
function panTo() {
  // 이동할 위도 경도 위치를 생성합니다
  var moveLatLon = new kakao.maps.LatLng(
    changed_coordinate[0],
    changed_coordinate[1]
  );

  // 지도 중심을 부드럽게 이동시킵니다
  // 만약 이동할 거리가 지도 화면보다 크면 부드러운 효과 없이 이동합니다
  map.panTo(moveLatLon);
}

//   // HTML5의 geolocation으로 사용할 수 있는지 확인합니다
//   if (navigator.geolocation) {
//     // GeoLocation을 이용해서 접속 위치를 얻어옵니다
//     navigator.geolocation.getCurrentPosition(function (position) {
//       var lat = position.coords.latitude, // 위도
//         lon = position.coords.longitude; // 경도

//       var locPosition = new kakao.maps.LatLng(lat, lon), // 마커가 표시될 위치를 geolocation으로 얻어온 좌표로 생성합니다
//         message = '<div style="padding:5px;">현재 위치</div>'; // 인포윈도우에 표시될 내용입니다

//       // 마커와 인포윈도우를 표시합니다
//       displayMarker(locPosition, message);
//     });
//   } else {
//     // HTML5의 GeoLocation을 사용할 수 없을때 마커 표시 위치와 인포윈도우 내용을 설정합니다

//     var locPosition = new kakao.maps.LatLng(33.450701, 126.570667),
//       message = "geolocation을 사용할수 없어요..";

//     displayMarker(locPosition, message);
//   }

// 유저의 선호 지역을 가져와 바로 맵으로 띄워주는 함수
function findUserPreferLocation() {
  let prefer_city = document.querySelector(".template_variable_city")
    .textContent;
  let prefer_gu = document.querySelector(".template_variable_gu").textContent;
  console.log(prefer_city);
  let gu_coordinate_list;
  let seoul_gu_coordinate = {
    강남구: [37.5173319258532, 127.047377408384],
    송파구: [37.5145909234015, 127.105922243305],
    서초구: [37.4835924256371, 127.032693842117],
    강동구: [37.5301933196159, 127.123792501252],
    관악구: [37.4783683761333, 126.951561853868],
    영등포구: [37.5263671784802, 126.896278443882],
    강서구: [37.5509646154244, 126.849533759514],
    양천구: [37.5169884752609, 126.866501409661],
    구로구: [37.4954330863648, 126.88750531451],
    금천구: [37.4568411485785, 126.895456780023],
    종로구: [37.5731294715895, 126.979230043705],
    중구: [37.563814978331, 126.997555182057],
    동대문구: [37.5745229817122, 127.039657001091],
    중랑구: [37.6065432383919, 127.092820287004],
    마포구: [37.5662141900954, 126.901955141101],
    용산구: [37.5324310391314, 126.990582345331],
    성동구: [37.563427205337, 127.036930141185],
    광진구: [37.5385583136667, 127.082385189457],
    은평구: [37.6028246477271, 126.928945504408],
    서대문구: [37.579161863979, 126.9368156604],
    성북구: [37.5893588153919, 127.016702905651],
    강북구: [37.6397513275882, 127.025538071854],
    도봉구: [37.6686914100284, 127.04721049936],
    노원구: [37.6543617567057, 127.056430475216],
  };
  let city_list = { 서울: seoul_gu_coordinate };
  if (prefer_city === "서울") {
    gu_coordinate_list = city_list["서울"];
    gu_coordinate = gu_coordinate_list[prefer_gu];
    let prefer_LatLon = new kakao.maps.LatLng(
      gu_coordinate[0],
      gu_coordinate[1]
    );
    map.setCenter(prefer_LatLon);
  }
  return gu_coordinate_list;
}

//도시를 선택했을 때 해당 도시의 구가 다음 select box에 뜰 수 있게 하는 함수
function addressKindChange(e) {
  let city;
  let seoul = [
    "강남구",
    "송파구",
    "서초구",
    "강동구",
    "관악구",
    "영등포구",
    "강서구",
    "양천구",
    "구로구",
    "금천구",
    "종로구",
    "중구",
    "동대문구",
    "중랑구",
    "마포구",
    "용산구",
    "성동구",
    "광진구",
    "은평구",
    "서대문구",
    "성북구",
    "강북구",
    "도봉구",
    "노원구",
  ];
  let target = document.querySelector("#gu");

  if (e.value == "서울특별시") {
    city = seoul;
  }
  for (x in city) {
    let opt = document.createElement("option");
    opt.value = city[x];
    opt.innerHTML = city[x];
    target.appendChild(opt);
  }
}

// 지도에 마커와 인포윈도우를 표시하는 함수입니다
function displayMarker(locPosition, message) {
  // 마커를 생성합니다
  var marker = new kakao.maps.Marker({
    map: map,
    position: locPosition,
  });

  var iwContent = message, // 인포윈도우에 표시할 내용
    iwRemoveable = true;

  // 인포윈도우를 생성합니다
  var infowindow = new kakao.maps.InfoWindow({
    content: iwContent,
    removable: iwRemoveable,
  });

  // 인포윈도우를 마커위에 표시합니다
  infowindow.open(map, marker);

  // 지도 중심좌표를 접속위치로 변경합니다
  map.setCenter(locPosition);
}

function map_reset(e) {
  // 선택한 구에 해당하는 좌표를 저장하고 있는 딕셔너리
  let gu_coordinate = {
    강남구: [37.5173319258532, 127.047377408384],
    송파구: [37.5145909234015, 127.105922243305],
    서초구: [37.4835924256371, 127.032693842117],
    강동구: [37.5301933196159, 127.123792501252],
    관악구: [37.4783683761333, 126.951561853868],
    영등포구: [37.5263671784802, 126.896278443882],
    강서구: [37.5509646154244, 126.849533759514],
    양천구: [37.5169884752609, 126.866501409661],
    구로구: [37.4954330863648, 126.88750531451],
    금천구: [37.4568411485785, 126.895456780023],
    종로구: [37.5731294715895, 126.979230043705],
    중구: [37.563814978331, 126.997555182057],
    동대문구: [37.5745229817122, 127.039657001091],
    중랑구: [37.6065432383919, 127.092820287004],
    마포구: [37.5662141900954, 126.901955141101],
    용산구: [37.5324310391314, 126.990582345331],
    성동구: [37.563427205337, 127.036930141185],
    광진구: [37.5385583136667, 127.082385189457],
    은평구: [37.6028246477271, 126.928945504408],
    서대문구: [37.579161863979, 126.9368156604],
    성북구: [37.5893588153919, 127.016702905651],
    강북구: [37.6397513275882, 127.025538071854],
    도봉구: [37.6686914100284, 127.04721049936],
    노원구: [37.6543617567057, 127.056430475216],
  };
  let siblings = Array.from($(e).siblings());
  let choosed_city = siblings.filter((node) => node.className == "choose_city");
  let selected_city = Array.from(choosed_city[0].childNodes).filter(
    (node) => node.className == "selected_city"
  );
  let selected_city_options = Array.from(selected_city[0].childNodes);

  //사용자가 지정한 도시 이름 = selected_city_option[0].value
  selected_city_option = selected_city_options.filter(
    (node) => node.nodeName == "OPTION" && node.selected
  );
  // console.log(selected_city_option[0].value);

  let choosed_gu = siblings.filter((node) => node.className == "choose_gu");
  let selected_gu = Array.from(choosed_gu[0].childNodes).filter(
    (node) => node.className == "selected_gu"
  );
  let selected_gu_options = Array.from(selected_gu[0].childNodes);

  //사용자가 지정한 구이름 = selected_gu_option[0].value
  selected_gu_option = selected_gu_options.filter(
    (node) => node.nodeName == "OPTION" && node.selected
  );

  // console.log(selected_option[0].value);
  // 주소-좌표 변환 객체를 생성합니다
  var geocoder = new kakao.maps.services.Geocoder();

  //사용자가 선택한 옵션을 토대로 주소 파싱
  let search_address =
    selected_city_option[0].value + " " + selected_gu_option[0].value;

  // 주소로 좌표를 검색합니다
  geocoder.addressSearch(search_address, function (result, status) {
    // 정상적으로 검색이 완료됐으면
    if (status === kakao.maps.services.Status.OK) {
      var coords = new kakao.maps.LatLng(result[0].y, result[0].x);

      // 결과값으로 받은 위치를 마커로 표시합니다
      var marker = new kakao.maps.Marker({
        map: map,
        position: coords,
      });

      markers.push(marker);
      hideMarkers();

      // 인포윈도우로 장소에 대한 설명을 표시합니다
      // var infowindow = new kakao.maps.InfoWindow({
      //   content:
      //     '<div style="width:150px;text-align:center;padding:6px 0;">요기입니당!</div>',
      // });
      // infowindow.open(map, marker);

      map.setCenter(coords);
      // console.log(coords.getLat(), coords.getLng());
    }
  });
}
