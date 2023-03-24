// import 'dart:convert';

// import 'package:http/http.dart' as http;

// class Member {
//   String baseUrl = "https://reqres.in/api/users?page=2";
//   // String TOKEN = "your_token_here";

//   Future<List> getAllMember() async {
//     print(baseUrl);
//     try {
//       var response =
//           await http.get(Uri.parse(baseUrl), headers: <String, String>{
//         'Content-Type': 'application/json;charset=UTF-8',
//         // 'Authorization':'Bearer $TOKEN',
//       });

//       if (response.statusCode == 200) {
//         return jsonDecode(response.body);
//       } else {
//         return Future.error('Server Error');
//       }
//     } catch (e) {
//       return Future.error(e);
//     }
//   }
// }
import 'dart:convert';

import 'package:http/http.dart' as http;

class Member {
  String baseUrl = "http://127.0.0.1:8000/myapp/aiotlab/?format=json";

  // String TOKEN = "your_token_here";

  Future<Map<String, dynamic>> getAllMember() async {
    print(baseUrl);
    try {
      var response =
          await http.get(Uri.parse(baseUrl), headers: <String, String>{
        'Content-Type': 'application/json;charset=UTF-8',
        // 'Authorization':'Bearer $TOKEN',
      });

      if (response.statusCode == 200) {
        return jsonDecode(response.body);
      } else {
        return Future.error('Server Error');
      }
    } catch (e) {
      return Future.error(e);
    }
  }
}
