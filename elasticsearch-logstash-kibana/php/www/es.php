<?php
require 'vendor/autoload.php';

$client = Elasticsearch\ClientBuilder::create()->setHosts(['http://elasticsearch:9200'])->build();
//新增
$params=[
    'index' => 'goods',
    'id'    => '48',
    'body'  => [
        'id' => 48,
        'goods_type_id' => 1,
        'category_id' => 46,
        'stock' => 0,
        'title' => '短袖男2021夏季新款潮流学生大码韩版休闲百搭宽松上衣体恤男',
        'goods_number' => '',
        'url' => '',
        'desc' => '',
        'min_price' => 990,
        'max_price' => 990,
        'image' => '/data/upload/2021-06-14/162365797798176.jpg',
        'images' => '/data/upload/2021-06-14/162365797798176.jpg',
        'content' => 'abc',
        'status' => 1,
        'sort' => 0,
        'delete_time' => 0,
        'create_time' => 1623658077,
        'update_time' => 1623812910,
    ]
];
$response = $client->create($params);
var_dump($response);

//搜索
//$params = [
//    'index' => 'goods',
//    'body'  => [
//        'query' => [
//            'match' => [
//                'title' => '短袖男2021夏季新款潮流学生大码韩版休闲百搭宽松上衣体恤男'
//            ]
//        ]
//    ]
//];
//
//$response = $client->search($params);
//var_dump($response);

//删除
//$params = [
//    'index' => 'goods',
//    'id'    => 48
//];
//$response = $client->delete($params);
//var_dump($response);