/* 
 Licensed under the Apache License, Version 2.0

 http://www.apache.org/licenses/LICENSE-2.0
 */
using System;
using System.Xml.Serialization;
using System.Collections.Generic;

    [XmlRoot(ElementName = "joint")]
    public class Joint1
    {
        [XmlAttribute(AttributeName = "name")]
        public string Name { get; set; }
        [XmlAttribute(AttributeName = "x")]
        public string X { get; set; }
        [XmlAttribute(AttributeName = "y")]
        public string Y { get; set; }
        [XmlAttribute(AttributeName = "z")]
        public string Z { get; set; }
    }

    [XmlRoot(ElementName = "frame")]
    public class Frame
    {
    [XmlElement(ElementName = "joint")]
    public List<Joint1> Joint { get; set; } = new List<Joint1>();
    }

    [XmlRoot(ElementName = "sign")]
    public class Sign
    {
    [XmlElement(ElementName = "frame")]
    public List<Frame> Frame { get; set; } = new List<Frame>();
        [XmlAttribute(AttributeName = "name")]
        public string Name { get; set; }
    }

    [XmlRoot(ElementName = "signs")]
    public class Signs
    {
         [XmlElement(ElementName = "sign")]
         public Sign Sign { get; set; } = new Sign();
    }
